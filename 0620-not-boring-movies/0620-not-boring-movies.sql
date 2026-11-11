SELECT id , movie , description , rating FROM Cinema
WHERE NOT description = 'boring' AND id%2
ORDER BY rating DESC;