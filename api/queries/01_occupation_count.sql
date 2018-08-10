SELECT * FROM onet_occu
NATURAL JOIN ostarnet_interface
NATURAL JOIN (
	SELECT ostarnetid, count(ostarnetid) as count FROM job
    WHERE job.postdate < '2018-06-18' AND job.postdate > '2018-06-10'
    GROUP BY ostarnetid
) AS j
;
