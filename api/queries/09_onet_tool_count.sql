SELECT
commodity.commodityname AS 'label_EN',
temp2.toolcount AS 'value'
FROM
(
	SELECT occu_has_tool.tooltype, occu_has_tool.commoditycode, occu_has_tool.toolexample, sum(jobcount) AS toolcount FROM
	(
		SELECT ostarnetid, count(ostarnetid) as jobcount FROM job
		WHERE job.postdate < '2018-06-15' AND job.postdate > '2018-06-10'
		GROUP BY ostarnetid
	) AS temp1

	LEFT JOIN ostarnet_interface
	ON ostarnet_interface.ostarnetid = temp1.ostarnetid

	LEFT JOIN occu_has_tool
	ON ostarnet_interface.ostarnetsoc = occu_has_tool.ostarnetsoc

	GROUP BY occu_has_tool.commoditycode
) AS temp2

LEFT JOIN commodity
ON temp2.commoditycode = commodity.commoditycode
