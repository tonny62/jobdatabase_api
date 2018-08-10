SELECT elementid, sum(count), ostarnetsoc, elementname FROM (
	SELECT ostarnet_interface.ostarnetid, occu_has_skill.ostarnetsoc, occu_has_skill.elementid, element.elementname, count.count FROM ostarnet_interface
	LEFT JOIN occu_has_skill ON ostarnet_interface.ostarnetsoc = occu_has_skill.ostarnetsoc
	LEFT JOIN element ON occu_has_skill.elementid = element.elementid
	LEFT JOIN (
			SELECT ostarnetid, count(ostarnetid) as count FROM job
            WHERE job.postdate < '2018-06-15' AND job.postdate > '2018-06-10'
            GROUP BY ostarnetid
	) AS count
ON count.ostarnetid = ostarnet_interface.ostarnetid) AS large
GROUP BY elementid
