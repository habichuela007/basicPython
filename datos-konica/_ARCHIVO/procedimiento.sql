BEGIN
    DECLARE fin INT DEFAULT FALSE;
    DECLARE CTASBAL VARCHAR(50); 
    DECLARE CONTADOR INT DEFAULT 1;
    DECLARE EJER1 INT DEFAULT YEAR(NOW());
    DECLARE PERIOD1 INT DEFAULT MONTH(NOW())-1;
    DECLARE PERCTAS INT;
    DECLARE EJERCTAS INT;    
    DECLARE FECCTAS DATE;
	 DECLARE NOMCTAS VARCHAR(50);
	 DECLARE VALPASA FLOAT;
	 DECLARE mensaje VARCHAR(100);
	 DECLARE NUMERO INT;
    
    DECLARE cuentas CURSOR FOR SELECT DISTINCT CUENTA AS CTASBAL FROM BALANCE_GENERAL ORDER BY CUENTA;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET fin = TRUE;

    OPEN cuentas;
    DELETE FROM BALANCES;
    SELECT COUNT(DISTINCT CUENTA) INTO NUMERO FROM BALANCE_GENERAL;
    REPEAT
        FETCH cuentas INTO CTASBAL;
         SELECT BGE.EJERCICIO INTO EJERCTAS FROM BALANCE_GENERAL BGE WHERE BGE.CUENTA = CTASBAL AND BGE.FECHA = (SELECT MIN(BG.FECHA) FROM BALANCE_GENERAL BG WHERE BG.CUENTA = BGE.CUENTA);
         SELECT BGP.PERIODO   INTO PERCTAS FROM BALANCE_GENERAL BGP WHERE BGP.CUENTA = CTASBAL AND BGP.FECHA = (SELECT MIN(BG.FECHA) FROM BALANCE_GENERAL BG WHERE BG.CUENTA = BGP.CUENTA);
         SELECT UNIQUE BGP.NOMBRE    INTO NOMCTAS FROM BALANCE_GENERAL BGP WHERE BGP.CUENTA = CTASBAL;
         
            WHILE EJERCTAS <= EJER1 DO  
            
                WHILE PERCTAS <= 12 DO   
                    IF (EJERCTAS < EJER1 OR (EJERCTAS = EJER1 AND PERCTAS <= PERIOD1)) THEN
                    		SET FECCTAS = NULL;
                    		SELECT BGP.VALOR_UNO INTO VALPASA FROM BALANCE_GENERAL BGP WHERE BGP.CUENTA = CTASBAL AND BGP.EJERCICIO = EJERCTAS AND BGP.PERIODO = PERCTAS;
					 			SELECT LAST_DAY(CONCAT(EJERCTAS, '-', PERCTAS, '-01')) INTO FECCTAS;
                        INSERT INTO BALANCES (TIPO,FECHA,CUENTA,NOMBRE,VALOR_UNO) VALUES ('BALANCE GENERAL',FECCTAS,CTASBAL,NOMCTAS,VALPASA);
                    END IF;                    
                    		SET PERCTAS = PERCTAS + 1;
                END WHILE;  
                
					               
                SET EJERCTAS = EJERCTAS + 1;                              
                SET PERCTAS = 1; 
            END WHILE;       
            
            SET CONTADOR = CONTADOR + 1;
            
    UNTIL CONTADOR > NUMERO END REPEAT;
    CLOSE cuentas;
    
    INSERT INTO BALANCES (TIPO,FECHA,CUENTA,NOMBRE,VALOR_UNO) 
	 SELECT TIPO, FECHA, CUENTA, NOMBRE, VALOR_UNO FROM ESTADO_RESULTADO ORDER BY CUENTA;
    
END