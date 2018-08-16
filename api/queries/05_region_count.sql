SELECT
	regioncount AS 'value',
    regionEN AS 'label_EN',
    regionTH AS 'label_TH'
FROM
(
	SELECT province.regionid, sum(temp1.provincecount) AS regioncount FROM
	(
		SELECT provinceid, count(provinceid) AS provincecount FROM job
		WHERE job.postdate < '2018-06-15' AND job.postdate > '2018-06-10'
		GROUP BY provinceid
	) AS temp1
	LEFT JOIN province
	ON province.provinceid = temp1.provinceid
	GROUP BY province.regionid
) AS temp2
LEFT JOIN region
ON region.regionid = temp2.regionid
