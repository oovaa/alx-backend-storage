--  ranks country origins of bands, ordered by the number of (non-unique) fans
SELECT band_name, 2022 - formed AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam%' AND style LIKE '%rock%'
ORDER BY lifespan DESC;