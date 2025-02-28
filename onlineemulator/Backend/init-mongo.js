db = db.getSiblingDB('main_db'); // Switch to the main_db
db.createCollection('games'); // Create the games collection
db.createCollection('users'); // Create the users collection

db.games.insertMany([
  { name: 'Worms Armageddon', url: '/games/Worms_Armageddon/game.z64', s3_url: 's3://dan-terraform-s3/games/Worms_Armageddon/game.z64', core: 'n64' },
  { name: 'EarthWorm Jim', url: '/games/Earthworm_Jim/game.z64', s3_url: 's3://dan-terraform-s3/games/EarthWorm_Jim/game.sfc', core: 'snes' },
  { name: 'Pokemon FireRed', url: '/games/Pokemon_FireRed/game.gba', s3_url: 's3://dan-terraform-s3/games/Pokemon_FireRed/game.gba', core: 'gba' }
]);

db.users.insertOne({ username: 'dan', password: 'hellofromfuture' }); 
  