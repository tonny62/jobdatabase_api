SELECT major.majorid, major.majornameEN, major.majornameTH, major.facultyid, majorcount FROM major
LEFT JOIN
	(
	SELECT majorid, count(majorid) AS majorcount FROM
		(
		SELECT jobid FROM job
		WHERE job.postdate < '2018-06-15' AND job.postdate > '2018-06-10'
		) AS temp
	LEFT JOIN job_has_major
	ON temp.jobid = job_has_major.jobid
	GROUP BY majorid
	) AS temp2
ON temp2.majorid = major.majorid
