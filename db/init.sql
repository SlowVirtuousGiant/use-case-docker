DROP TABLE IF EXISTS weather;       
CREATE TABLE public.weather (
	"time" varchar NOT NULL,
	temperature_2m varchar NOT NULL,
	apparent_temperature varchar NOT NULL,
	precipitation varchar NOT NULL
);