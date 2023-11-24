BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE usuario VARCHAR(50);
    DECLARE impresiones_periodo INT;
    DECLARE periodo VARCHAR(7);
    DECLARE ultimo_dia DATE;
    DECLARE last_no_of_originals_counter INT DEFAULT NULL;
    DECLARE current_no_of_originals_counter INT;
    DECLARE current_fecha_contador DATETIME;
    DECLARE current_impresora VARCHAR(50);

    -- Cursor for 223_A1UG011006937
    DECLARE cur1 CURSOR FOR
        SELECT user_name, no_of_originals_counter, fecha_contador, impresora
        FROM 223_A1UG011006937
        ORDER BY user_name, fecha_contador;      
    -- Cursor for 224e_A61H011006163
    DECLARE cur2 CURSOR FOR
        SELECT user_name, no_of_originals_counter, fecha_contador, impresora
        FROM 224e_A61H011006163
        ORDER BY user_name, fecha_contador;
    -- Cursor for 227_A7AK011010262
    DECLARE cur3 CURSOR FOR
        SELECT user_name, no_of_originals_counter, fecha_contador, impresora
        FROM 227_A7AK011010262
        ORDER BY user_name, fecha_contador;
    -- Cursor for 283_A1UF011003305
    DECLARE cur4 CURSOR FOR
        SELECT user_name, no_of_originals_counter, fecha_contador, impresora
        FROM 283_A1UF011003305
        ORDER BY user_name, fecha_contador;
    -- Cursor for 283_A1UF012000896
    DECLARE cur5 CURSOR FOR
        SELECT user_name, no_of_originals_counter, fecha_contador, impresora
        FROM 283_A1UF012000896
        ORDER BY user_name, fecha_contador;
    -- Cursor for 363_A1UE011015445
    DECLARE cur6 CURSOR FOR
        SELECT user_name, no_of_originals_counter, fecha_contador, impresora
        FROM 363_A1UE011015445
        ORDER BY user_name, fecha_contador;
    -- Cursor for 363_A1UE011016227
    DECLARE cur7 CURSOR FOR
        SELECT user_name, no_of_originals_counter, fecha_contador, impresora
        FROM 363_A1UE011016227
        ORDER BY user_name, fecha_contador;
    -- Cursor for 363_A1UE011020415
    DECLARE cur8 CURSOR FOR
        SELECT user_name, no_of_originals_counter, fecha_contador, impresora
        FROM 363_A1UE011020415
        ORDER BY user_name, fecha_contador;
    -- Cursor for 363_A1UE011024719
    DECLARE cur9 CURSOR FOR
        SELECT user_name, no_of_originals_counter, fecha_contador, impresora
        FROM 363_A1UE011024719
        ORDER BY user_name, fecha_contador;
    -- Cursor for 363_A1UE011103699
    DECLARE cur10 CURSOR FOR
        SELECT user_name, no_of_originals_counter, fecha_contador, impresora
        FROM 363_A1UE011103699
        ORDER BY user_name, fecha_contador;
    -- Cursor for 363_A1UE011104367
    DECLARE cur11 CURSOR FOR
        SELECT user_name, no_of_originals_counter, fecha_contador, impresora
        FROM 363_A1UE011104367
        ORDER BY user_name, fecha_contador;
    -- Cursor for 364e_A61F011024714
    DECLARE cur12 CURSOR FOR
        SELECT user_name, no_of_originals_counter, fecha_contador, impresora
        FROM 364e_A61F011024714
        ORDER BY user_name, fecha_contador;
    -- Cursor for 552_A2WV011008573
    DECLARE cur13 CURSOR FOR
        SELECT user_name, no_of_originals_counter, fecha_contador, impresora
        FROM 552_A2WV011008573
        ORDER BY user_name, fecha_contador;
    -- Cursor for C227_A798011501042
    DECLARE cur14 CURSOR FOR
        SELECT user_name, no_of_originals_counter, fecha_contador, impresora
        FROM C227_A798011501042
        ORDER BY user_name, fecha_contador;
    -- Cursor for C452_A0P2011001067
    DECLARE cur15 CURSOR FOR
        SELECT user_name, no_of_originals_counter, fecha_contador, impresora
        FROM C452_A0P2011001067
        ORDER BY user_name, fecha_contador;
    -- Cursor for C554e_A5AY011013622
    DECLARE cur16 CURSOR FOR
        SELECT user_name, no_of_originals_counter, fecha_contador, impresora
        FROM C554e_A5AY011013622
        ORDER BY user_name, fecha_contador;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN cur1;
    read_loop1: LOOP
        FETCH cur1 INTO usuario, current_no_of_originals_counter, current_fecha_contador, current_impresora;

        IF done THEN
            LEAVE read_loop1;
        END IF;

        IF last_no_of_originals_counter IS NOT NULL THEN
            SET impresiones_periodo = GREATEST(0, current_no_of_originals_counter - last_no_of_originals_counter);
            SET periodo = CONCAT(YEAR(current_fecha_contador), LPAD(WEEK(current_fecha_contador, 3), 2, '0'));
            SET ultimo_dia = DATE_ADD(current_fecha_contador, INTERVAL 6 - DAYOFWEEK(current_fecha_contador) DAY);
            INSERT INTO totales (usuario, impresiones_periodo, periodo, ultimo_dia, fecha_contador, impresora)
            VALUES (usuario, impresiones_periodo, periodo, ultimo_dia, current_fecha_contador, current_impresora);
        END IF;

        SET last_no_of_originals_counter = current_no_of_originals_counter;
    END LOOP;
    CLOSE cur1;

    OPEN cur2;
    read_loop2: LOOP
        FETCH cur2 INTO usuario, current_no_of_originals_counter, current_fecha_contador, current_impresora;

        IF done THEN
            LEAVE read_loop2;
        END IF;

        IF last_no_of_originals_counter IS NOT NULL THEN
            SET impresiones_periodo = GREATEST(0, current_no_of_originals_counter - last_no_of_originals_counter);
            SET periodo = CONCAT(YEAR(current_fecha_contador), LPAD(WEEK(current_fecha_contador, 3), 2, '0'));
            SET ultimo_dia = DATE_ADD(current_fecha_contador, INTERVAL 6 - DAYOFWEEK(current_fecha_contador) DAY);
            INSERT INTO totales (usuario, impresiones_periodo, periodo, ultimo_dia, fecha_contador, impresora)
            VALUES (usuario, impresiones_periodo, periodo, ultimo_dia, current_fecha_contador, current_impresora);
        END IF;

        SET last_no_of_originals_counter = current_no_of_originals_counter;
    END LOOP;
    CLOSE cur2;

    OPEN cur3;
    read_loop3: LOOP
        FETCH cur3 INTO usuario, current_no_of_originals_counter, current_fecha_contador, current_impresora;

        IF done THEN
            LEAVE read_loop3;
        END IF;

        IF last_no_of_originals_counter IS NOT NULL THEN
            SET impresiones_periodo = GREATEST(0, current_no_of_originals_counter - last_no_of_originals_counter);
            SET periodo = CONCAT(YEAR(current_fecha_contador), LPAD(WEEK(current_fecha_contador, 3), 2, '0'));
            SET ultimo_dia = DATE_ADD(current_fecha_contador, INTERVAL 6 - DAYOFWEEK(current_fecha_contador) DAY);
            INSERT INTO totales (usuario, impresiones_periodo, periodo, ultimo_dia, fecha_contador, impresora)
            VALUES (usuario, impresiones_periodo, periodo, ultimo_dia, current_fecha_contador, current_impresora);
        END IF;

        SET last_no_of_originals_counter = current_no_of_originals_counter;
    END LOOP;
    CLOSE cur3;

    OPEN cur4;
    read_loop4: LOOP
        FETCH cur4 INTO usuario, current_no_of_originals_counter, current_fecha_contador, current_impresora;

        IF done THEN
            LEAVE read_loop4;
        END IF;

        IF last_no_of_originals_counter IS NOT NULL THEN
            SET impresiones_periodo = GREATEST(0, current_no_of_originals_counter - last_no_of_originals_counter);
            SET periodo = CONCAT(YEAR(current_fecha_contador), LPAD(WEEK(current_fecha_contador, 3), 2, '0'));
            SET ultimo_dia = DATE_ADD(current_fecha_contador, INTERVAL 6 - DAYOFWEEK(current_fecha_contador) DAY);
            INSERT INTO totales (usuario, impresiones_periodo, periodo, ultimo_dia, fecha_contador, impresora)
            VALUES (usuario, impresiones_periodo, periodo, ultimo_dia, current_fecha_contador, current_impresora);
        END IF;

        SET last_no_of_originals_counter = current_no_of_originals_counter;
    END LOOP;
    CLOSE cur4;

    OPEN cur5;
    read_loop5: LOOP
        FETCH cur5 INTO usuario, current_no_of_originals_counter, current_fecha_contador, current_impresora;

        IF done THEN
            LEAVE read_loop5;
        END IF;

        IF last_no_of_originals_counter IS NOT NULL THEN
            SET impresiones_periodo = GREATEST(0, current_no_of_originals_counter - last_no_of_originals_counter);
            SET periodo = CONCAT(YEAR(current_fecha_contador), LPAD(WEEK(current_fecha_contador, 3), 2, '0'));
            SET ultimo_dia = DATE_ADD(current_fecha_contador, INTERVAL 6 - DAYOFWEEK(current_fecha_contador) DAY);
            INSERT INTO totales (usuario, impresiones_periodo, periodo, ultimo_dia, fecha_contador, impresora)
            VALUES (usuario, impresiones_periodo, periodo, ultimo_dia, current_fecha_contador, current_impresora);
        END IF;

        SET last_no_of_originals_counter = current_no_of_originals_counter;
    END LOOP;
    CLOSE cur5;

    OPEN cur6;
    read_loop6: LOOP
        FETCH cur6 INTO usuario, current_no_of_originals_counter, current_fecha_contador, current_impresora;

        IF done THEN
            LEAVE read_loop6;
        END IF;

        IF last_no_of_originals_counter IS NOT NULL THEN
            SET impresiones_periodo = GREATEST(0, current_no_of_originals_counter - last_no_of_originals_counter);
            SET periodo = CONCAT(YEAR(current_fecha_contador), LPAD(WEEK(current_fecha_contador, 3), 2, '0'));
            SET ultimo_dia = DATE_ADD(current_fecha_contador, INTERVAL 6 - DAYOFWEEK(current_fecha_contador) DAY);
            INSERT INTO totales (usuario, impresiones_periodo, periodo, ultimo_dia, fecha_contador, impresora)
            VALUES (usuario, impresiones_periodo, periodo, ultimo_dia, current_fecha_contador, current_impresora);
        END IF;

        SET last_no_of_originals_counter = current_no_of_originals_counter;
    END LOOP;
    CLOSE cur6;

    OPEN cur7;
    read_loop7: LOOP
        FETCH cur7 INTO usuario, current_no_of_originals_counter, current_fecha_contador, current_impresora;

        IF done THEN
            LEAVE read_loop7;
        END IF;

        IF last_no_of_originals_counter IS NOT NULL THEN
            SET impresiones_periodo = GREATEST(0, current_no_of_originals_counter - last_no_of_originals_counter);
            SET periodo = CONCAT(YEAR(current_fecha_contador), LPAD(WEEK(current_fecha_contador, 3), 2, '0'));
            SET ultimo_dia = DATE_ADD(current_fecha_contador, INTERVAL 6 - DAYOFWEEK(current_fecha_contador) DAY);
            INSERT INTO totales (usuario, impresiones_periodo, periodo, ultimo_dia, fecha_contador, impresora)
            VALUES (usuario, impresiones_periodo, periodo, ultimo_dia, current_fecha_contador, current_impresora);
        END IF;

        SET last_no_of_originals_counter = current_no_of_originals_counter;
    END LOOP;
    CLOSE cur7;

    OPEN cur8;
    read_loop8: LOOP
        FETCH cur8 INTO usuario, current_no_of_originals_counter, current_fecha_contador, current_impresora;

        IF done THEN
            LEAVE read_loop8;
        END IF;

        IF last_no_of_originals_counter IS NOT NULL THEN
            SET impresiones_periodo = GREATEST(0, current_no_of_originals_counter - last_no_of_originals_counter);
            SET periodo = CONCAT(YEAR(current_fecha_contador), LPAD(WEEK(current_fecha_contador, 3), 2, '0'));
            SET ultimo_dia = DATE_ADD(current_fecha_contador, INTERVAL 6 - DAYOFWEEK(current_fecha_contador) DAY);
            INSERT INTO totales (usuario, impresiones_periodo, periodo, ultimo_dia, fecha_contador, impresora)
            VALUES (usuario, impresiones_periodo, periodo, ultimo_dia, current_fecha_contador, current_impresora);
        END IF;

        SET last_no_of_originals_counter = current_no_of_originals_counter;
    END LOOP;
    CLOSE cur8;

    OPEN cur9;
    read_loop9: LOOP
        FETCH cur9 INTO usuario, current_no_of_originals_counter, current_fecha_contador, current_impresora;

        IF done THEN
            LEAVE read_loop9;
        END IF;

        IF last_no_of_originals_counter IS NOT NULL THEN
            SET impresiones_periodo = GREATEST(0, current_no_of_originals_counter - last_no_of_originals_counter);
            SET periodo = CONCAT(YEAR(current_fecha_contador), LPAD(WEEK(current_fecha_contador, 3), 2, '0'));
            SET ultimo_dia = DATE_ADD(current_fecha_contador, INTERVAL 6 - DAYOFWEEK(current_fecha_contador) DAY);
            INSERT INTO totales (usuario, impresiones_periodo, periodo, ultimo_dia, fecha_contador, impresora)
            VALUES (usuario, impresiones_periodo, periodo, ultimo_dia, current_fecha_contador, current_impresora);
        END IF;

        SET last_no_of_originals_counter = current_no_of_originals_counter;
    END LOOP;
    CLOSE cur9;

    OPEN cur10;
    read_loop10: LOOP
        FETCH cur10 INTO usuario, current_no_of_originals_counter, current_fecha_contador, current_impresora;

        IF done THEN
            LEAVE read_loop10;
        END IF;

        IF last_no_of_originals_counter IS NOT NULL THEN
            SET impresiones_periodo = GREATEST(0, current_no_of_originals_counter - last_no_of_originals_counter);
            SET periodo = CONCAT(YEAR(current_fecha_contador), LPAD(WEEK(current_fecha_contador, 3), 2, '0'));
            SET ultimo_dia = DATE_ADD(current_fecha_contador, INTERVAL 6 - DAYOFWEEK(current_fecha_contador) DAY);
            INSERT INTO totales (usuario, impresiones_periodo, periodo, ultimo_dia, fecha_contador, impresora)
            VALUES (usuario, impresiones_periodo, periodo, ultimo_dia, current_fecha_contador, current_impresora);
        END IF;

        SET last_no_of_originals_counter = current_no_of_originals_counter;
    END LOOP;
    CLOSE cur10;

    OPEN cur11;
    read_loop11: LOOP
        FETCH cur11 INTO usuario, current_no_of_originals_counter, current_fecha_contador, current_impresora;

        IF done THEN
            LEAVE read_loop11;
        END IF;

        IF last_no_of_originals_counter IS NOT NULL THEN
            SET impresiones_periodo = GREATEST(0, current_no_of_originals_counter - last_no_of_originals_counter);
            SET periodo = CONCAT(YEAR(current_fecha_contador), LPAD(WEEK(current_fecha_contador, 3), 2, '0'));
            SET ultimo_dia = DATE_ADD(current_fecha_contador, INTERVAL 6 - DAYOFWEEK(current_fecha_contador) DAY);
            INSERT INTO totales (usuario, impresiones_periodo, periodo, ultimo_dia, fecha_contador, impresora)
            VALUES (usuario, impresiones_periodo, periodo, ultimo_dia, current_fecha_contador, current_impresora);
        END IF;

        SET last_no_of_originals_counter = current_no_of_originals_counter;
    END LOOP;
    CLOSE cur11;

    OPEN cur12;
    read_loop12: LOOP
        FETCH cur12 INTO usuario, current_no_of_originals_counter, current_fecha_contador, current_impresora;

        IF done THEN
            LEAVE read_loop12;
        END IF;

        IF last_no_of_originals_counter IS NOT NULL THEN
            SET impresiones_periodo = GREATEST(0, current_no_of_originals_counter - last_no_of_originals_counter);
            SET periodo = CONCAT(YEAR(current_fecha_contador), LPAD(WEEK(current_fecha_contador, 3), 2, '0'));
            SET ultimo_dia = DATE_ADD(current_fecha_contador, INTERVAL 6 - DAYOFWEEK(current_fecha_contador) DAY);
            INSERT INTO totales (usuario, impresiones_periodo, periodo, ultimo_dia, fecha_contador, impresora)
            VALUES (usuario, impresiones_periodo, periodo, ultimo_dia, current_fecha_contador, current_impresora);
        END IF;

        SET last_no_of_originals_counter = current_no_of_originals_counter;
    END LOOP;
    CLOSE cur12;

    OPEN cur13;
    read_loop13: LOOP
        FETCH cur13 INTO usuario, current_no_of_originals_counter, current_fecha_contador, current_impresora;

        IF done THEN
            LEAVE read_loop13;
        END IF;

        IF last_no_of_originals_counter IS NOT NULL THEN
            SET impresiones_periodo = GREATEST(0, current_no_of_originals_counter - last_no_of_originals_counter);
            SET periodo = CONCAT(YEAR(current_fecha_contador), LPAD(WEEK(current_fecha_contador, 3), 2, '0'));
            SET ultimo_dia = DATE_ADD(current_fecha_contador, INTERVAL 6 - DAYOFWEEK(current_fecha_contador) DAY);
            INSERT INTO totales (usuario, impresiones_periodo, periodo, ultimo_dia, fecha_contador, impresora)
            VALUES (usuario, impresiones_periodo, periodo, ultimo_dia, current_fecha_contador, current_impresora);
        END IF;

        SET last_no_of_originals_counter = current_no_of_originals_counter;
    END LOOP;
    CLOSE cur13;

    OPEN cur14;
    read_loop14: LOOP
        FETCH cur14 INTO usuario, current_no_of_originals_counter, current_fecha_contador, current_impresora;

        IF done THEN
            LEAVE read_loop14;
        END IF;

        IF last_no_of_originals_counter IS NOT NULL THEN
            SET impresiones_periodo = GREATEST(0, current_no_of_originals_counter - last_no_of_originals_counter);
            SET periodo = CONCAT(YEAR(current_fecha_contador), LPAD(WEEK(current_fecha_contador, 3), 2, '0'));
            SET ultimo_dia = DATE_ADD(current_fecha_contador, INTERVAL 6 - DAYOFWEEK(current_fecha_contador) DAY);
            INSERT INTO totales (usuario, impresiones_periodo, periodo, ultimo_dia, fecha_contador, impresora)
            VALUES (usuario, impresiones_periodo, periodo, ultimo_dia, current_fecha_contador, current_impresora);
        END IF;

        SET last_no_of_originals_counter = current_no_of_originals_counter;
    END LOOP;
    CLOSE cur14;

    OPEN cur15;
    read_loop15: LOOP
        FETCH cur15 INTO usuario, current_no_of_originals_counter, current_fecha_contador, current_impresora;

        IF done THEN
            LEAVE read_loop15;
        END IF;

        IF last_no_of_originals_counter IS NOT NULL THEN
            SET impresiones_periodo = GREATEST(0, current_no_of_originals_counter - last_no_of_originals_counter);
            SET periodo = CONCAT(YEAR(current_fecha_contador), LPAD(WEEK(current_fecha_contador, 3), 2, '0'));
            SET ultimo_dia = DATE_ADD(current_fecha_contador, INTERVAL 6 - DAYOFWEEK(current_fecha_contador) DAY);
            INSERT INTO totales (usuario, impresiones_periodo, periodo, ultimo_dia, fecha_contador, impresora)
            VALUES (usuario, impresiones_periodo, periodo, ultimo_dia, current_fecha_contador, current_impresora);
        END IF;

        SET last_no_of_originals_counter = current_no_of_originals_counter;
    END LOOP;
    CLOSE cur15;

    OPEN cur16;
    read_loop16: LOOP
        FETCH cur16 INTO usuario, current_no_of_originals_counter, current_fecha_contador, current_impresora;

        IF done THEN
            LEAVE read_loop16;
        END IF;

        IF last_no_of_originals_counter IS NOT NULL THEN
            SET impresiones_periodo = GREATEST(0, current_no_of_originals_counter - last_no_of_originals_counter);
            SET periodo = CONCAT(YEAR(current_fecha_contador), LPAD(WEEK(current_fecha_contador, 3), 2, '0'));
            SET ultimo_dia = DATE_ADD(current_fecha_contador, INTERVAL 6 - DAYOFWEEK(current_fecha_contador) DAY);
            INSERT INTO totales (usuario, impresiones_periodo, periodo, ultimo_dia, fecha_contador, impresora)
            VALUES (usuario, impresiones_periodo, periodo, ultimo_dia, current_fecha_contador, current_impresora);
        END IF;

        SET last_no_of_originals_counter = current_no_of_originals_counter;
    END LOOP;
    CLOSE cur16;
END