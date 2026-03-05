import unittest
    from workflow.motion_lattice_engine import DeterministicWorkflowEngine, MotionLatticeState
    
    class TestGovernance(unittest.TestCase):
        def test_onst_enforcement(self):
            engine = DeterministicWorkflowEngine()
            state = MotionLatticeState("IDLE", "EXECUTE", {"requires_human_onst": True})
            with self.assertRaises(Exception):
                engine.transition_state("agent_01", state)
    
    if __name__ == "__main__":
        unittest.main()
    
