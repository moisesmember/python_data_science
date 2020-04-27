-- CREATE OR REPLACE VIEW VIEW_STATICS_SUICIDIO AS
SELECT
	SUICIDIO.AGE,
	SUICIDIO.SEX,
	COUNT(SUICIDIO.YEAR) QTDE_REGISTROS,
	SUM(SUICIDIO.SUICIDES_NO) NUM_TOTAL_CASOS,
	(
	   trunc(((SUM(SUICIDIO.SUICIDES_NO)*100)/( SELECT SUM(B.SUICIDES_NO) TOTAL FROM VIEW_SUICIDIO B )), 2)
	) PERCIL_TOTAL_CASOS,
	MODE() WITHIN GROUP (ORDER BY SUICIDIO.SUICIDES_NO) AS MODA_NUM_SUICIDIO,
	trunc( AVG(SUICIDIO.SUICIDES_NO), 2 ) MEDIA_NUM_SUICIDIO,
	trunc( median(SUICIDIO.SUICIDES_NO), 0 ) MEDIANA_NUM_SUICIDIO,
	MAX(SUICIDIO.SUICIDES_NO)-MIN(SUICIDIO.SUICIDES_NO) AMPLITUDE_NUM_SUICIDIO
FROM VIEW_SUICIDIO SUICIDIO
	GROUP BY SUICIDIO.AGE, SUICIDIO.SEX
	ORDER BY SUICIDIO.SEX;
	