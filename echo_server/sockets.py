from socketio.namespace import BaseNamespace
from socketio.sdjango import namespace
import logging
logging.basicConfig(level=logging.DEBUG)

@namespace('/echo')
class EchoNamespace(BaseNamespace):
    def on_msg(self, msg):
    	print "test1"
        pkt = dict(type='event',
                   name='msg',
                   args='Someone said: {0}'.format(msg),
                   endpoint=self.ns_name)
        print "test2"
        for sessid, socket in self.socket.server.sockets.iteritems():
            socket.send_packet(pkt)