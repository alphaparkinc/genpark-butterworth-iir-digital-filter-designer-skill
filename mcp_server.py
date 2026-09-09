"""MCP Server for Butterworth IIR Filter Skill."""
import json
import sys
from client import ButterworthLowpass

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            req_id = req.get("id")
            method = req.get("method")
            params = req.get("params", {})

            if method == "tools/list":
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "tools": [{
                            "name": "apply_butterworth_filter",
                            "description": "Filter noisy signal with Butterworth lowpass filter",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "signal": {"type": "array", "items": {"type": "number"}},
                                    "cutoff_freq": {"type": "number"},
                                    "sampling_rate": {"type": "number"}
                                },
                                "required": ["signal", "cutoff_freq", "sampling_rate"]
                            }
                        }]
                    }
                }
            elif method == "tools/call":
                args = params.get("arguments", {})
                flt = ButterworthLowpass(args["cutoff_freq"], args["sampling_rate"])
                res_sig = flt.filter_signal(args["signal"])
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {"content": [{"type": "text", "text": json.dumps({"filtered_signal": res_sig})}]}
                }
            else:
                res = {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}
            print(json.dumps(res), flush=True)
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32000, "message": str(e)}}
            print(json.dumps(err), flush=True)

if __name__ == "__main__":
    main()
