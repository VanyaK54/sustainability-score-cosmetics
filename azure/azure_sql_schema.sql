
---

#### 📄 `azure_sql_schema.sql`

```sql
CREATE TABLE sustainability_scores (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(255),
    ingredient_score FLOAT,
    packaging_score FLOAT,
    sustainability_score FLOAT
);
