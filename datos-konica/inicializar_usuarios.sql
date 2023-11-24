--LISTADO DE TABLAS--
223_A1UG011006937 
224e_A61H011006163
227_A7AK011010262 
283_A1UF011003305 
283_A1UF012000896 
363_A1UE011015445 
363_A1UE011016227 
363_A1UE011020415 
363_A1UE011024719 
363_A1UE011103699 
363_A1UE011104367 
364e_A61F011024714
552_A2WV011008573 
C227_A798011501042
C452_A0P2011001067
C554e_A5AY011013622

--OBTENER EL LISTADO DE USUARIOS CUYO PRIMER REPORTE NO TIENE CERO
SELECT t.user_name, t.no_of_originals_counter, t.fecha_contador
FROM C554e_A5AY011013622 t
INNER JOIN (
    SELECT user_name, MIN(fecha_contador) AS primera_fecha
    FROM C554e_A5AY011013622
    GROUP BY user_name
) sub
ON t.user_name = sub.user_name AND t.fecha_contador = sub.primera_fecha
WHERE t.no_of_originals_counter <> 0;