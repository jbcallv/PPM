def trace_memory_usage(self, frame, event, arg):
        """Callback for sys.settrace"""
        if event == "call":
            self.trace_stack.append(frame)
        elif event == "return":
            self.trace_stack.pop()
        return self.trace_stack

    def __del__(self):
        # Restore the original trace function on exit
        sys.settrace(self.original_trace_function)

