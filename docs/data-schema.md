# Data Schema

### Raw Files
| Column | Type | Description |
|---------|------|-------------|
| product_id | int | Unique product ID |
| product_name | string | Product name |
| price | float | Listed price |
| currency | string | Currency type |
| source | string | Website name |
| timestamp | date | Date of extraction |

### Processed Data
| Column | Type | Description |
|---------|------|-------------|
| product_name | string | Product name |
| avg_price | float | Average competitor price |
| recommended_price | float | Target price suggestion |
