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

SELECT
  user_name,
  MAX(no_of_originals_counter) - MIN(no_of_originals_counter) AS diferencia,
  DATE_FORMAT(fecha_contador, '%Y%u') AS semana
FROM 227_A7AK011010262
GROUP BY user_name, semana;

SELECT
  user_name,
  MAX(no_of_originals_counter) - MIN(no_of_originals_counter) AS diferencia,
  DATE_FORMAT(fecha_contador, '%Y%u') AS periodo
FROM C227_A798011501042
GROUP BY user_name, periodo
HAVING diferencia <> 0;

SELECT
  user_name,
  SUM(no_of_originals_counter) AS suma_valores,
  DATE_FORMAT(fecha_contador, '%Y%u') AS periodo
FROM C227_A798011501042
GROUP BY user_name, periodo
HAVING suma_valores <> 0;
