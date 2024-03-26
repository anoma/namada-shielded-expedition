# Validator instructions for hard fork and state migration

The hard fork is planned to take place at block height `237907` and will upgrade Namada to `v0.32.1`. The following instructions to accomplish this are detailed below. Most of the commands require the use of the `namadan` binary, which is the same as running `namada node`. The use of `namadan` and `namada node` are interchangeable.

## Hosted files and materials

The team is providing special files that are needed in order to execute the migration properly. Some of the necessary files are provided in the [hard_fork directory](hard_fork/) of this repository. Other locations are noted below if the files are hosted elsewhere. These are:

- `namada-0.31.10`: binaries for all architectures can be found at https://github.com/anoma/namada/releases/tag/v0.31.10
- `namada-0.32.1`: binaries for all architectures can be found at https://github.com/anoma/namada/releases/tag/v0.32.1
- `make-db-migration`: linux binary needed to perform the state migration
- `wasm`: two files - `checksums.json` and `vp_user wasm` are provideď to upgrade the user VP

In the following instructions, we will refer to different binaries with the following different names.

- `namadan`: the current runtime from `v0.31.9`
- `namadan-0.31.10`: the same exact behavior as the `v0.31.9` runtime but also has extra migration features built in. All steps below that are performed with `namadan` can also be performed with `namadan-0.31.10`.
- `namadan-0.32.1`: the new runtime from `v0.32.1`.

## Before the hard fork

1. Shut down your node and restart it using `namadan ledger run-until --block-height 237907 --suspend`. This will run your ledger and suspend it automatically at the provided block height `237907`, where the hard fork is planned.
2. Once you reach height `237907`, you may have to shut down your node with `Ctrl+C`.
3. Backup your state by zipping your base directory (you might have the default of `.local/share/namada/shielded-expedition.88f17d1d14`) and keeping it in a nice place.

## Executing the hard fork

There will be several steps to perform here. At a high-level, you need to manually manipulate the database after producing a file called `migrations.json` and then restart your node with the new runtime binaries.

### Getting `migrations.json`

Node operators should attempt to produce the `migrations.json` file themselves. This file can only be produced properly once the chain is halted at block height `237907`. The following instructions depend on certain files existing on your machine relative to the directory from which you run certain binaries. Typically, you should execute all commands from the home directory of your machine.

1. Run `namadan-0.31.10 ledger query-db --db-key conversion_state --hash 05E2FD0BEBD54A05AAE349BBDE61F90893F09A72850EFD4F69060821EC5DE65F --db-column-family state > conversion_state.txt`. Make sure the produced `conversion_state.txt` file is in your current working directory.
2. Make a direcory called `wasm` in your current directory and then copy the new `vp_user.6065919f895d43099a567cb120ebdfa0c99c3ba4e803fe99159a14bd8f97f0ea.wasm` and `checksums.json` files from the [hard_fork directory](hard_fork/) into `wasm/`. This might involve remote copying the files onto your machine and then performing:
    ```
    mkdir wasm
    mv <some_path>/vp_user.6065919f895d43099a567cb120ebdfa0c99c3ba4e803fe99159a14bd8f97f0ea.wasm wasm/
    mv <some_path>/checksums.json wasm/
    ```
3. Run `./make-db-migration`, which requires that `conversion_state.txt` and the `wasm` directory are in the directory from which you run this command. Confirm that `migrations.json` is produced in your current directory as a result. You may have to first run `chmod +x make-db-migration` to make the binary executable.

Additionally, the Namada team will provide a `migrations.json` file on Github in the [hard_fork directory](hard_fork/) along with a `shasum` of the file. The team will only be able to generate this file once the chain has halted at the planned hard fork block height `237907`, as the contents of this file are dependent on the state at that block height. NOTE: it may be wise to wait until the Namada team has generated and posted the `migrations.json` file for verification before you continue with the next steps here.

While the hosted `migrations.json` file may be downloaded and used, the team encourages operators to try to produce the file themselves and verify that the `shasum` of your own file matches that of the hosted one. You can do this by running `shasum migrations.json`, which will give you a hash.

### State migration

Now that you have `migrations.json`:

1. Run `namadan-0.32.1 ledger update-db --path migrations.json --block-height 237907 --dry-run` and make sure there are no errors.
1. Run `namadan-0.32.1 ledger update-db --path migrations.json --block-height 237907` (no `--dry-run`). This will update the DB and try to progress the ledger by two blocks before suspending itself again. The ledger will only be able to progress the two blocks and finish this step if enough voting power is online with this command in execution. After two blocks, the ledger will halt. You may need to kill it yourself with `CTRL+C`, or it may exit for you.
2. Once the ledger is stopped after updating the DB, run the ledger as normal with the new binaries: `namadan-0.32.1 ledger run`.
3. At this point, the chain has fully upgraded and forked, and you should use the `v0.32.1` runtime for all functionality.

## Shielded syncing after the hard fork

The hard fork will also make properly scanning for old MASP notes by running `namadac shielded-sync` a bit trickier. After the hard fork, the client will no longer be able to make RPC calls to cometBFT to query for MASP notes before block height `237907`, when the hard fork takes place. As a result, any preivously shielded tokens that remain shielded through the hard for will likely be inaccessible after the hard fork.

1. In `v0.32.1`, `shielded-sync` has a new option `--from-height` that will start the MASP note scanning at the given height. When you query from a `v0.32.1` node, please for at least the first time, use `namadac shielded-sync --from-height 237907`. Afterward, you will not need to use the `--from-height` option anymore
2. We also encourage users to unshield all of their shielded tokens before the hard fork, and then reshield after.
3. Shielding tokens after the hard fork will work as it normally has otherwise.