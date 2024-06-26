from pb.relay_node_pb2_grpc import RelayNodeServicer
from ai.ai_logic import AILogic
from multiprocessing import Queue
from json import dumps
import pb.relay_node_pb2 as relay__node__pb2
from utils.logger import Logger

class RelayNodeServicer(RelayNodeServicer):
    def __init__(self, action_queue_1: Queue, action_queue_2: Queue, player_turn):
        self.action_queue_1 = action_queue_1
        self.action_queue_2 = action_queue_2
        # player turn is not really used
        self.player_turn = player_turn
        self.ai = AILogic()
        super().__init__()

    def processAi(self, request, context):
        # Logger.log(request.player_id)
        Logger.log(f"Received from {request.player_id} with shoot_detected {request.shoot_detected}")
        action = None
        if request.test_action:
            action = request.test_action
        elif not request.shoot_detected:
            try:
                action = self.ai.process(request.values)
                print(f"Predicted action by {request.player_id} is {action}")
            except:
                action = "gun"
        else:
            action = "gun"

        if request.player_id == 1:
            self.action_queue_1.put(dumps({ 
                "action": action,
                "player_id": request.player_id,
            }))
        elif request.player_id == 2:
            self.action_queue_2.put(dumps({ 
                "action": action,
                "player_id": request.player_id,
            }))
        
        return relay__node__pb2.FromRelayNodeResponse()
    
    def processGameState(self, request, context):
        return relay__node__pb2.GameStateResponse()