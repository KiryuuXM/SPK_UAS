CREATE TABLE Samsung_Galaxy (
    Model VARCHAR(255),
    RAM VARCHAR(10),
    Storage VARCHAR(10),
    Processor VARCHAR(255),
    Screen_Size VARCHAR(20),
    Price DECIMAL(12, 2),
    Battery_Capacity VARCHAR(20)
);

INSERT INTO Samsung_Galaxy (Model, RAM, Storage, Processor, Screen_Size, Price, Battery_Capacity)
VALUES
    ('Samsung Galaxy S23 5G', '8 GB', '256 GB', 'Snapdragon 8 Gen 2', '6.1 inch', 13999000, '3900 mAh'),
    ('Samsung Galaxy S23+ 5G', '8 GB', '512 GB', 'Snapdragon 8 Gen 2', '6.6 inch', 15000000, '4700 mAh'),
    ('Samsung Galaxy S23 Ultra 5G', '12 GB', '512 GB', 'Snapdragon 8 Gen 2', '6.8 inch', 25999000, '5000 mAh'),
    ('Samsung Galaxy S22 5G', '8 GB', '256 GB', 'Snapdragon 8 Gen 1', '6.1 inch', 11200000, '3700 mAh'),
    ('Samsung Galaxy S22 Plus 5G', '8 GB', '256 GB', 'Snapdragon 8 Gen 1', '6.6 inch', 13499000, '4500 mAh'),
    ('Samsung Galaxy S22 Ultra 5G', '12 GB', '256 GB', 'Snapdragon 8 Gen 1', '6.6 inch', 14500000, '5000 mAh'),
    ('Samsung Galaxy S21 FE 5G', '8 GB', '256 GB', 'Exynos 2100', '6.4 inch', 6700000, '4500 mAh'),
    ('Samsung Galaxy S21 5G', '8 GB', '256 GB', 'Exynos 2100', '6.2 inch', 12000000, '4000 mAh'),
    ('Samsung Galaxy S21+ 5G', '8 GB', '256 GB', 'Exynos 2100', '6.7 inch', 14300000, '4800 mAh'),
    ('Samsung Galaxy S21 Ultra 5G', '16 GB', '512 GB', 'Exynos 2100', '6.8 inch', 19500000, '5000 mAh');
    
   select * from samsung_galaxy;