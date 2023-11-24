BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE usuario VARCHAR(255);
    DECLARE impresiones_periodo INT;
    DECLARE periodo VARCHAR(7);
    DECLARE ultimo_dia DATE;
    DECLARE last_no_of_originals_counter INT DEFAULT NULL;
    DECLARE current_no_of_originals_counter INT;
    DECLARE current_fecha_contador DATETIME;
    DECLARE current_impresora VARCHAR(255);

    -- Cambia la definición del cursor para incluir la nueva columna fecha_contador
    DECLARE cur CURSOR FOR
        SELECT user_name, no_of_originals_counter, fecha_contador, impresora
        FROM C452_A0P2011001067
        ORDER BY user_name, fecha_contador, impresora;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    
    OPEN cur;

    read_loop: LOOP
        FETCH cur INTO usuario, current_no_of_originals_counter, current_fecha_contador, current_impresora;

        IF done THEN
            LEAVE read_loop;
        END IF;

        IF last_no_of_originals_counter IS NOT NULL THEN
            SET impresiones_periodo = GREATEST(0, current_no_of_originals_counter - last_no_of_originals_counter);
            SET periodo = CONCAT(YEAR(current_fecha_contador), LPAD(WEEK(current_fecha_contador, 3), 2, '0'));
            SET ultimo_dia = DATE_ADD(current_fecha_contador, INTERVAL 6 - DAYOFWEEK(current_fecha_contador) DAY);

            -- Asegúrate de que la tabla 'totales' tenga la columna fecha_contador
            INSERT INTO totales (usuario, impresiones_periodo, periodo, ultimo_dia, fecha_contador, impresora)
            VALUES (usuario, impresiones_periodo, periodo, ultimo_dia, current_fecha_contador, current_impresora);
        END IF;

        SET last_no_of_originals_counter = current_no_of_originals_counter;
    END LOOP;

    CLOSE cur;
END