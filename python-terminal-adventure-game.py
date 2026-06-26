import time
import numpy as np
import os

#define the start time of the game
start_time = time.time()
lives = 3



class collision_manager:
          #touching_the_enemy
          def __init__(self, the_game):
            self.outer = the_game

          #if you touched the enemy in level one
          def touching_player(self):
                      self.outer.New_map[self.outer.old_y, self.outer.old_x] = "."

                      self.outer.enemy1_position = [4, 1]
                      self.outer.old_y, self.outer.old_x = [4, 1]
                      self.outer.N_enemy_y, self.outer.N_enemy_x = self.outer.old_y, self.outer.old_x
                      self.outer.New_map[self.outer.old_y, self.outer.old_x] = "E"

                      self.outer.New_map[self.outer.player_y, self.outer.player_x] = "."

                      self.outer.player_x = 1
                      self.outer.player_y = 1
                      self.outer.the_player = [self.outer.player_y, self.outer.player_x]
                      self.outer.next_y, self.outer.next_x = [self.outer.player_y, self.outer.player_x]
                      self.outer.New_map[self.outer.player_y, self.outer.player_x] = "P"

                      self.outer.lives = self.outer.lives - 1
                      print('You have been eaten')
                      self.outer.New_map = self.outer.Map
                      return


          def touching2_player(self):
                      self.outer.New_map2[self.outer.old2_y, self.outer.old2_x] = "."
                      self.outer.New_map2[self.outer.old3_y, self.outer.old3_x] = "."

                      self.outer.enemy2_position = [4, 4]
                      self.outer.enemy3_position = [4, 8]
                      self.outer.old2_y, self.outer.old2_x = [4, 4]
                      self.outer.old3_y, self.outer.old3_x = [4, 8]
                      self.outer.N_enemy2_y, self.outer.N_enemy2_x = [4, 4]
                      self.outer.N_enemy3_y, self.outer.N_enemy3_x = [4, 8]
                      self.outer.New_map2[self.outer.old2_y, self.outer.old2_x] = 'E'
                      self.outer.New_map2[self.outer.old3_y, self.outer.old3_x] = 'E'


                      self.outer.New_map2[self.outer.player_y, self.outer.player_x] = "."

                      self.outer.player_x = 1
                      self.outer.player_y = 1
                      self.outer.the_player = [1,1]
                      self.outer.next_y, self.outer.next_x = [1,1]
                      self.outer.New_map2[self.outer.player_y, self.outer.player_x] = 'P'

                      self.outer.lives = self.outer.lives - 1
                      print('You have been eaten')
                      self.outer.New_map2 = self.outer.Map2
                      return

#define the enemies behaiveur
class enemy:
             def __init__(self, the_game):
                     self.outer = the_game
             def enemy_movement(self):
                  rng = np.random.default_rng()
                  enemy_move_axis = []
                  for m in range(6):
                      n = rng.integers(low=-1, high=2)
                      enemy_move_axis.append(n)
                  a_b = enemy_move_axis[0], enemy_move_axis[1]
                  x_y = enemy_move_axis[2], enemy_move_axis[3]
                  i_j = enemy_move_axis[4], enemy_move_axis[5]

                  if self.outer.won == False:
                        self.outer.enemy1_position = [a + b for a, b in zip(self.outer.enemy1_position, a_b)]
                        self.outer.N_enemy_y, self.outer.N_enemy_x = self.outer.enemy1_position
                        self.enemy1_action()
                        return

                  else:
                       self.outer.enemy2_position = [a + b for a, b in zip(self.outer.enemy2_position, x_y)]
                       self.outer.N_enemy2_y, self.outer.N_enemy2_x = self.outer.enemy2_position

                       self.outer.enemy3_position = [a + b for a, b in zip(self.outer.enemy3_position, i_j)]
                       self.outer.N_enemy3_y, self.outer.N_enemy3_x = self.outer.enemy3_position


                       self.enemy2_action()
                       self.enemy3_action()


             def enemy1_action(self):
                  if self.outer.New_map[self.outer.N_enemy_y, self.outer.N_enemy_x] in ('#', 'K', 'D'):
                     self.outer.N_enemy_y, self.outer.N_enemy_x = [self.outer.old_y, self.outer.old_x]
                     self.outer.enemy1_position = [self.outer.old_y, self.outer.old_x]

                  elif self.outer.New_map[self.outer.N_enemy_y, self.outer.N_enemy_x] == ".":
                      self.outer.New_map[self.outer.old_y, self.outer.old_x] = "."
                      self.outer.New_map[self.outer.N_enemy_y, self.outer.N_enemy_x] = 'E'
                      self.outer.old_y, self.outer.old_x = [self.outer.N_enemy_y, self.outer.N_enemy_x]

                  elif self.outer.New_map[self.outer.N_enemy_y, self.outer.N_enemy_x] == 'P':
                      self.outer.collision_manager.touching_player()

             def enemy2_action(self):
                  if self.outer.New_map2[self.outer.N_enemy2_y, self.outer.N_enemy2_x] in ('#', 'K', 'D'):
                     self.outer.N_enemy2_y, self.outer.N_enemy2_x = [self.outer.old2_y, self.outer.old2_x]
                     self.outer.enemy2_position = [self.outer.old2_y, self.outer.old2_x]

                  elif self.outer.New_map2[self.outer.N_enemy2_y, self.outer.N_enemy2_x] == ".":
                      self.outer.New_map2[self.outer.old2_y, self.outer.old2_x] = "."
                      self.outer.New_map2[self.outer.N_enemy2_y, self.outer.N_enemy2_x] = 'E'
                      self.outer.old2_y, self.outer.old2_x = [self.outer.N_enemy2_y, self.outer.N_enemy2_x]

                  elif self.outer.New_map2[self.outer.N_enemy2_y, self.outer.N_enemy2_x] == 'P':
                      self.outer.collision_manager.touching2_player()

             def enemy3_action(self):
                  if self.outer.New_map2[self.outer.N_enemy3_y, self.outer.N_enemy3_x] in ('#', 'K', 'D'):
                     self.outer.N_enemy3_y, self.outer.N_enemy3_x = [self.outer.old3_y, self.outer.old3_x]
                     self.outer.enemy3_position = [self.outer.old3_y, self.outer.old3_x]

                  elif self.outer.New_map2[self.outer.N_enemy3_y, self.outer.N_enemy3_x] == ".":
                      self.outer.New_map2[self.outer.old3_y, self.outer.old3_x] = "."
                      self.outer.New_map2[self.outer.N_enemy3_y, self.outer.N_enemy3_x] = 'E'
                      self.outer.old3_y, self.outer.old3_x = [self.outer.N_enemy3_y, self.outer.N_enemy3_x]

                  elif self.outer.New_map2[self.outer.N_enemy3_y, self.outer.N_enemy3_x] == 'P':
                      self.outer.collision_manager.touching2_player()


class the_player_class:
              def __init__(self, the_game):
                   self.outer = the_game

              def game_ready_check(self):
                self.outer.time_elapsed = time.time() - self.outer.start_time
                self.outer.remaining_time = self.outer.Game_duration - self.outer.time_elapsed
                if self.outer.remaining_time <= 0:
                   print("Time is out")
                   time.sleep(5)
                   os._exit(0)

                #if you ready for round2
                if self.outer.won == True:
                          #the show of the game
                          print("you have", self.outer.lives, "lives", 'Remaining time is : ', self.outer.remaining_time)
                          print(self.outer.New_map2)

                          #check the validation of the inputs
                          self.user_choice = input('use ethir W or a or s or d your choice : ').lower()
                          if self.user_choice not in self.outer.valid_options:
                                print("Invalid input! Please use only W, A, S, or D.")
                                print()
                                return
                          self.player_movement()
                          self.outer.game_levels.round2()
                          return

                #if you still in round1
                #the show of the game
                print("you have", self.outer.lives, "lives", 'Remaining time is : ', self.outer.remaining_time)
                print(self.outer.New_map)

                #check the validation of the inputs
                self.user_choice = input('use ethir W or a or s or d your choice : ').lower()
                if self.user_choice not in self.outer.valid_options:
                     print("Invalid input! Please use only W, A, S, or D.")
                     print()
                     return
                self.player_movement()
                self.outer.game_levels.round1()


              def player_movement(self):
                  #player_movement(y, x)
                  self.outer.next_y, self.outer.next_x = self.outer.player_y, self.outer.player_x
                  if self.user_choice == 'w':
                     self.outer.next_y -= 1  # للأعلى
                  elif self.user_choice == 's':
                       self.outer.next_y += 1  # للأسفل
                  elif self.user_choice == 'a':
                       self.outer.next_x -= 1  # لليسار
                  elif self.user_choice == 'd':
                       self.outer.next_x += 1  # للليمين



class game_levels:
              def __init__(self, the_game):
                    self.outer = the_game

              def round1(self):

                 self.outer.enemy.enemy_movement()
                 self.destination = self.outer.New_map[self.outer.next_y, self.outer.next_x]
                 if self.destination == '#':
                  print("wrong movement")
                  return

                 elif self.destination == self.outer.free_space:
                  self.outer.New_map[self.outer.player_y, self.outer.player_x] = "."
                  self.outer.New_map[self.outer.next_y, self.outer.next_x] = 'P'
                  self.outer.player_x, self.outer.player_y = [self.outer.next_x, self.outer.next_y]
                  self.outer.the_player = [self.outer.player_y, self.outer.player_x]
                  return

                 elif self.destination == self.outer.the_key:
                  self.outer.New_map[self.outer.player_y, self.outer.player_x] = "."
                  self.outer.New_map[self.outer.next_y, self.outer.next_x] = 'P'
                  self.outer.player_x, self.outer.player_y = [self.outer.next_x, self.outer.next_y]
                  self.outer.the_player = [self.outer.player_y, self.outer.player_x]
                  self.outer.key_hold = True
                  return

                 elif self.destination == self.outer.the_enemy:
                  self.outer.collision_manager.touching_player()

                 elif self.destination == self.outer.the_door and self.outer.key_hold == True:
                  print("you won", '         ', 'the game end')
                  self.outer.Game_duration = self.outer.Game_duration + 90
                  self.outer.won = True
                  self.outer.key_hold = False
                  self.outer.player_x = 1
                  self.outer.player_y = 1
                  self.outer.the_player = [1,1]
                  return

                 elif self.destination == self.outer.the_door and self.outer.key_hold == False:
                  print('you need to find the key')
                  return

                 else:
                  print('use ethir W or A or S or D your choice')
                  return

              def round2(self):
                     #call the enemy to start move
                     self.outer.enemy.enemy_movement()

                     self.destination = self.outer.New_map2[self.outer.next_y, self.outer.next_x]
                     if self.destination == '#':
                        print("wrong movement")
                        return

                     elif self.destination == ".":
                        self.outer.New_map2[self.outer.player_y, self.outer.player_x] = "."
                        self.outer.New_map2[self.outer.next_y, self.outer.next_x] = 'P'
                        self.outer.player_x, self.outer.player_y = [self.outer.next_x, self.outer.next_y]
                        self.outer.the_player = [self.outer.player_y, self.outer.player_x]
                        return

                     elif self.destination == 'K':
                        self.outer.New_map2[self.outer.player_y, self.outer.player_x] = "."
                        self.outer.New_map2[self.outer.next_y, self.outer.next_x] = 'P'
                        self.outer.player_x, self.outer.player_y = [self.outer.next_x, self.outer.next_y]
                        self.outer.the_player = [self.outer.player_y, self.outer.player_x]
                        self.outer.key_hold = True
                        return

                     elif self.destination == self.outer.the_enemy:
                        self.outer.collision_manager.touching2_player()

                     elif self.destination == self.outer.the_door and self.outer.key_hold == True:
                        print("you won", '         ', 'the game end')
                        time.sleep(10)
                        os._exit(0)

                     elif self.destination == self.outer.the_door and self.outer.key_hold == False:
                        print('you need to find the key')
                        return
                     else:
                        print('use ethir W or a or s or d your choice!')
                        return

#now we will difine the game steps
class the_game:
  def __init__(self, start_time, lives):
           #the game main parts
           self.the_key = 'K'
           self.the_enemy = 'E'
           self.the_door = 'D'
           self.free_space = '.'

           #the game limitation
           self.lives = lives
           self.key_hold = False
           self.won = False
           self.valid_options = ['w','a','s','d']

           #the game map
           self.Map = np.array([['#','#','#','#','#','#','#','#','#','#'],['#','P','.','.','.','.','#','.','.','#'],['#','.','.','#','#','.','#','K','.','#'],['#','.','.','.','.','.','#','.','.','#'],['#','E','#','#','#','.','.','.','.','#'],['#','.','.','.','.','#','#','D','#','#'],['#','#','#','#','#','#','#','#','#','#']])
           self.New_map = self.Map.copy()
           self.Map2 = np.array([['#','#','#','#','#','#','#','#','#','#'],['#','P','.','#','.','.','#','.','K','#'],['#','.','.','#','.','#','#','.','.','#'],['#','.','.','.','.','#','.','.','#','#'],['#','.','#','.','E','.','.','.','E','#'],['#','D','#','.','.','.','.','.','#','#'],['#','#','#','#','#','#','#','#','#','#']])
           self.New_map2 = self.Map2.copy()

           #the player position
           self.player_y = 1
           self.player_x = 1
           self.the_player = [self.player_y, self.player_x]
           self.next_y = self.player_y
           self.next_x = self.player_x

           #the enemies position
           self.enemy1_y = 4
           self.enemy1_x = 1
           self.enemy1_position = [self.enemy1_y, self.enemy1_x]
           self.enemy2_y = 4
           self.enemy2_x = 4
           self.enemy2_position = [self.enemy2_y, self.enemy2_x]
           self.enemy3_y = 4
           self.enemy3_x = 8
           self.enemy3_position = [self.enemy3_y, self.enemy3_x]

           self.old_y, self.old_x = [self.enemy1_position[0], self.enemy1_position[1]]
           self.old2_y, self.old2_x = [self.enemy2_position[0], self.enemy2_position[1]]
           self.old3_y, self.old3_x = [self.enemy3_position[0], self.enemy3_position[1]]

           self.N_enemy_y, self.N_enemy_x = [self.enemy1_position[0], self.enemy1_position[1]]
           self.N_enemy2_y, self.N_enemy2_x = [self.enemy2_position[0], self.enemy2_position[1]]
           self.N_enemy3_y, self.N_enemy3_x = [self.enemy3_position[0], self.enemy3_position[1]]

           #the calculations of game time
           self.start_time = start_time
           self.Game_duration = 40

           #connect the inner classes
           self.collision_manager = collision_manager(self)
           self.enemy = enemy(self)
           self.the_player_class = the_player_class(self)
           self.game_levels = game_levels(self)






game = the_game(start_time, lives)


print('welcome to the game')


while game.lives > 0:
    game.the_player_class.game_ready_check()

else:
  time.sleep(5)
  os._exit(0)



