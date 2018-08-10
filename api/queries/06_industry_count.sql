SELECT industry.*, temp1.industrycount FROM
(
	SELECT industryid, count(industryid) AS industrycount
	FROM job
	LEFT JOIN company
	ON job.idcompany = company.idcompany
	WHERE job.postdate < '2018-06-15' AND job.postdate > '2018-06-10'
	GROUP BY industryid
) AS temp1
LEFT JOIN industry
ON industry.industryid = temp1.industryid
