import aiml
import os
class chatbot:
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'myaiml.aiml')
# Create the kernel and learn AIML files
    kernel = aiml.Kernel()
    def _init_(self):
        print 'Inside Init'
        # self.kernel.learn(self.file_path)
        self.kernel.respond("load aiml b")

    def replychat(self,InpStr,SessionKey):
        print 'Inside Replychat'
        self.kernel.learn(self.file_path)
        #self.kernel.respond("load aiml b")
        print self.file_path
        return self.kernel.respond(InpStr,sessionID = SessionKey)