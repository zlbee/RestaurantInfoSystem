INSERT INTO public.api_restaurant (id,name,"location",cuisine,rating,contact_id) VALUES
	 (1,'Pasta Paradise','Rome','Italian',4.5,1),
	 (2,'Curry King','Mumbai','Indian',4.7,5),
	 (3,'Sushi Suite','Tokyo','Japanese',4.9,6),
	 (4,'Taco T','Mexico City','Mexican',4.4,7),
	 (5,'Taco Bell','Mexico City','Mexican',4.7,11),
	 (6,'Taco Ring','Mexico City','Mexican',4.9,13);

 INSERT INTO public.api_contact (phone,email) VALUES
	 ('123-456-7890','info@pastaparadise.com'),
	 ('098-765-4321','contact@currykingdom.com'),
	 ('234-567-8901','reservations@sushisuite.com'),
	 ('345-678-9012','info@tacoterritory.mx'),
	 ('345-678-1290','info@tacobell.mx'),
	 ('345-678-1291','info@tacoring.mx');
