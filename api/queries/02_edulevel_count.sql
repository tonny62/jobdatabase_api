SELECT
	count AS 'value',
    edulevelnameEN AS 'label_EN',
    edulevelnameTH AS 'label_TH',
    temp2.edulevelid
FROM edulevel
LEFT JOIN
	(
	SELECT edulevelid, count(edulevelid) AS count FROM
		(
		SELECT jobid FROM job
		WHERE job.postdate < '2018-06-18' AND job.postdate > '2018-06-10'
		) AS temp
	LEFT JOIN job_has_edulevel
	ON temp.jobid = job_has_edulevel.jobid
	GROUP BY edulevelid
	) AS temp2
ON temp2.edulevelid = edulevel.edulevelid
