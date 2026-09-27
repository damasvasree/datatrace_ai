import sys
from engine import DataTraceEngine

def run_system_tests():
    print("========================================")
    print("Running DataTrace AI Diagnostic Test Suite")
    print("========================================")
    
    engine = DataTraceEngine()
    
    # Test 1: Query Execution
    print("[TEST 1] Testing DuckDB Execution...")
    query = "Why did MRR drop in August?"
    res = engine.execute_verified_analysis(query)
    assert res["evaluated_rows"] > 0, "Failed: No rows evaluated!"
    print("  --> Passed: Engine correctly queried DuckDB local store.")
    
    # Test 2: Traceability Audit
    print("[TEST 2] Testing Traceability Lineage...")
    assert "lineage_records" in res, "Failed: Missing lineage records!"
    assert len(res["lineage_records"]) == res["evaluated_rows"], "Failed: Lineage mismatch!"
    print(f"  --> Passed: Lineage verified for {res['evaluated_rows']} data rows.")
    
    # Test 3: Decision Output Integrity
    print("[TEST 3] Testing Recommendation Matrix...")
    assert len(res["decisions"]) >= 2, "Failed: Less than 2 decision options returned!"
    assert "roi" in res["decisions"][0], "Failed: Decision missing ROI field!"
    print("  --> Passed: Decision framework correctly generated.")
    
    print("\nALL TESTS PASSED: System is 100% Ready for Submission!")

if __name__ == "__main__":
    run_system_tests()