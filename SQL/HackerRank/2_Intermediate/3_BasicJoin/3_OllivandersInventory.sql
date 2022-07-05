-- id, age, coins, power Ron interested in, sort in desc power, desc age


-- point : power와 age별 최소 coins_needed에 해당하는 행만 출력

SELECT W.ID, P.AGE, W.COINS_NEEDED, W.POWER
FROM WANDS W
LEFT JOIN WANDS_PROPERTY P
ON W.CODE = P.CODE
WHERE P.IS_EVIL = 0
AND W.COINS_NEEDED = (
  SELECT MIN(COINS_NEEDED)
  FROM WANDS W1
  INNER JOIN WANDS_PROPERTY P1
  ON W1.CODE = P1.CODE
  WHERE P1.IS_EVIL = 0
  AND W1.POWER = W.POWER
  AND P1.AGE = P.AGE
)
ORDER BY 4 DESC, 2 DESC;