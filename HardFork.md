# Validator instructions for hard fork and state migration

The hard fork is planned to take place at block height `X`. The following instructions to accomplish this are detailed below.

## Hosted files and materials

The team is providing a couple sets of special binaries that are needed in order to execute the migration properly. At the moment, these are:

- `namada-0.31.9-MIG`: found at `<insert_link>`
- `namada-0.32.0-MIG`: found at `<insert_link>`

In the following instructions, we will refer to different binaries with the following different names.

- `namadan`: the current runtime from v0.31.9
- `namadan-0.31.9-MIG`: special runtime based on v0.31.9 with extra migration feature.
- `namadan-0.32.0`: the new runtime to which we are upgrading from the v0.32.0 release. These can be fetched from the release page on Github.
- `namadan-0.32.0-MIG`: special runtime based on v0.32.0 with extra migration feature.

Please note that `namadan-0.31.9-MIG` can be used to do everything that `namadan` can do, and likewise for v0.32.0.

We will also host a new wasm for the user VP, along with a new `checksums.json` file, which can be found at `<insert_link>`.

## Before the hard fork

1. Shut down your node and restart it using `namadan ledger run-until --block-height X --suspend`. This will run your ledger and suspend it automatically at the provided block height `X`, where the hard fork is planned.
2. Once you reach height `X`, you may have to shut down your node with `Ctrl+C`.
3. Backup your state by zipping your `.local/share/namada/shielded-expedition.88f17d1d14` directory and keeping it in a nice place.

## Executing the hard fork

There will be several steps to perform here. At a high-level, you need to manually manipulate the database using a file called `migrations.json` and then restart your node with the new runtime binaries.

### Getting `migrations.json`

Node operators should attempt to produce the `migrations.json` file themselves. At this moment, this requires building Namada from source somewhere. Please refer to https://github.com/anoma/namada/blob/main/README.md for instructions on how to do this.

You will need to build namada from source using [#2937](https://github.com/anoma/namada/pull/2937), which is the branch `brent/test-migration-from-0.31.9`. This is also the same branch that `namadan-0.31.9-MIG` is built from.

Given that you have built namada from source on this branch, follow these steps to produce `migrations.json`:

1. Go to the root directory of your Namada built from source
2. Run `namadan-0.31.9-MIG ledger query-db --db-key conversion_state --hash 05E2FD0BEBD54A05AAE349BBDE61F90893F09A72850EFD4F69060821EC5DE65F --db-column-family state > conversion_state.txt`
3. Copy the new `vp.wasm` and `checksums.json` files from `<insert_link>` into the `wasm/` directory relative to your current path (`namada/wasm/`).
4. Run `cargo run --example make-db-migration`, which should produce `migrations.json` in the current directory

Additionally, the Namada team will provide a `migrations.json` file on Github at `<insert_URL>` along with a `shasum` of the file. The team will only be able to generate this file once the chain has halted at the planned hard fork block height `X`, as the contents of this file are dependent on the state at that block height.

While the hosted `migrations.json` file may be downloaded and used, the team encourages operators to try to produce the file themselves and verify that the `shasum` of your own file matches that of the hosted one. You can do this by running `shasum migrations.json`, which will give you a hash.

### State migration

Now that you have `migrations.json`:

1. Run `namadan-0.32.0-MIG ledger update-db --path migrations.json --block-height X`. This will update the DB and try to progress the ledger by two blocks before suspending itself again. The ledger will only be able to progress the two blocks and finish this step if enough voting power is online with this command in execution. After two blocks, the ledger will halt. You may need to kill it yourself with `CTRL+C`, or it may exit for you.
2. Once the ledger is stopped after updating the DB, run the ledger as normal with the new binaries: `namadan-0.32.0 ledger run`.

### To-Do:
- give shielded sync instructions
- include all necessary files and the `shasum` of `migrations.json`
- choose the block height `X`
- maybe try to provide a special binary instead of requiring `cargo run --example make-db-migration`
