# Runbook

## Steps
1. Run scrapers in `src/extract/` to collect data.  
2. Execute `clean_merge_prices.py` to process and combine.  
3. Run `price_recommendation.py` for pricing logic.  
4. Upload results with `upload_to_datalake.py`.  
5. Launch dashboard via `streamlit run dashboard/app.py`.

## Troubleshooting
- Check CSV file encoding issues.
- Verify Azure connection string environment variable.
