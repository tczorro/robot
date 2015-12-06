import rgkit.rg as rg
class Robot:
    def act(self, game):
        self.game = game
        spawn_test = self._spawn_action()
        if spawn_test:
            return spawn_test
        return ["guard"]

    def _spawn_action(self):
        if Robot._spawn_test(self.location):
            normal, spawn = Robot._surrounding(self.location)
            print normal, spawn
            if normal:
                n_occu, n_unoccu = Robot._occupied_find(normal, self.game)
                if n_unoccu:
                    return ["move", rg.toward(self.location, n_unoccu[0])]
            if spawn:
                s_occu, s_unoccu = Robot._occupied_find(spawn, self.game)
                if s_unoccu:
                    return ["move", rg.toward(self.location, s_unoccu[0])]
        else:
            return None

    @staticmethod
    def _spawn_test(location):
        spot = rg.loc_types(location)
        if ("spawn") in spot:
            return True
        else:
            return False

    @staticmethod
    def _surrounding(location):
        normal = rg.locs_around(location, filter_out=('invalid', 'obstacle', 'spawn'))
        spawn = rg.locs_around(location, filter_out=('invalid', 'obstacle'))
        for i in spawn:
            if i in normal:
                spawn.remove(i)
        return normal, spawn

    @staticmethod
    def _occupied_find(locs, game):
        occupied = []
        unoccupied = []
        loc_len = len(locs)
        condition = [None] * loc_len
        for i in range(loc_len):
            if locs[i] in game.robots:
                condition[i] = "occupied"
                occupied.append(locs[i])
            else:
                condition[i] = "unoccupied"
                unoccupied.append(locs[i]) 
        return occupied, unoccupied

    @staticmethod
    def _test_friend_bot(my_player_id, loc, game):
        bot_player_id = game.robots[loc]['player_id']
        if bot_player_id == my_player_id:
            return "enemy"
        else:
            return "friend"


        # if self.location == rg.CENTER_POINT
        # return ["guard"]

        # for loc, bot in game.robots.iteritems():
        #     if bot.player_id != self.player_id:
        #         if rg.dist(loc, self.location) <= 1:
        #             return ["attack", loc]

        # return ["move", rg.toward(self.location, rg.CENTER_POINT)]
