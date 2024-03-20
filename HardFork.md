# Validator instructions for hard fork and state migration

The hard fork is planned to take place at block height `X`. The following instructions to accomplish this are detailed below.

## Before the hard fork

1. Shut down your node and restart it using `namadan ledger run-until --block-height X --suspend`. This will run your ledger and suspend it automatically at the provided block height `X`, where the hard fork is planned.
2. Once you reach height `X`, you may have to shut down your node with `Ctrl+C`.
3. Backup your state by zipping your `.local/share/namada/shielded-expedition.88f17d1d14` directory.

## Executing the hard fork

There will be several steps to perform here. At a high-level, you need to manually manipulate the database using a file called `migrations.json`, replace your existing wasms with new ones, and then restart your node with the new runtime binaries.

### Getting `migrations.json`

Node operators should attempt to produce the `migrations.json` file themselves. At the moment, this requires building Namada from source. Please refer to https://github.com/anoma/namada/blob/main/README.md for instructions for how to do this.

Given that you have Namada built from source, follow these steps to produce `migrations.json`:

1. Go to the root directory of Namada
2. Run `namadan ledger query-db --db-key conversion_state --hash 05E2FD0BEBD54A05AAE349BBDE61F90893F09A72850EFD4F69060821EC5DE65F --db-column-family state > conversion_state.txt`
3. Copy new `.wasm` and `checksums.json` files into the `wasm/` directory
4. Run `cargo run --example make-db-migration`, which will produce `migrations.json` in the current directory

Alternatively, the Namada team will provide a `migrations.json` file on Github at `<insert_URL>` along with a `shasum` of the file. While the hosted `migrations.json` file may be downloaded and used, the team encourages operators to try to produce the file themselves and verify that the `shasum` of your own file matches that of the hosted one.

### State migration

Now that you have `migrations.json`:

1. Run `namadan ledger update-db --path migrations.json --block-height X` (TODO: which binaries to use for this?). This will update the DB, progress the ledger a couple blocks (TODO: need to elaborate on this), and then shut it down again.
2. Run the ledger as normal with the new binaries: `namadan ledger run`

### To-Do:
- give shielded sync instructions
- include a `migrations.json` file with this PR, along with the `shasum`
- choose the block height `X`
- clearly specify which binaries to use at all steps
- clarify exactly when new wasms should be copied and where to get them
- clarify where to get binaries (everyone prob knows this though)

