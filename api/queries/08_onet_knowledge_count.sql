SELECT elementid, sum(count) AS knowledgeCount, elementname FROM (
	SELECT ostarnet_interface.ostarnetid, occu_has_knowledge.ostarnetsoc, occu_has_knowledge.elementid, element.elementname, count.count FROM ostarnet_interface
	LEFT JOIN occu_has_knowledge ON ostarnet_interface.ostarnetsoc = occu_has_knowledge.ostarnetsoc
	LEFT JOIN element ON occu_has_knowledge.elementid = element.elementid
	LEFT JOIN (
			SELECT ostarnetid, count(ostarnetid) as count FROM job
            WHERE job.postdate < '2018-06-15' AND job.postdate > '2018-06-10'
            GROUP BY ostarnetid
	) AS count
ON count.ostarnetid = ostarnet_interface.ostarnetid) AS large
GROUP BY elementid
