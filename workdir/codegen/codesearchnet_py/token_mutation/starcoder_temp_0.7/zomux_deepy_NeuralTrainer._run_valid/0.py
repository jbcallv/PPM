def _run_valid(self, epoch, valid_set, dry_run=False, save_path=None):
        """
        as one valid iteration, as for if to continue training.
        """
        valid_loader = DataLoader(valid_set, self.args.batch_size, shuffle=False, drop_last=False,
                                  collate_fn=self.collate_fn)

        if save_path is not None:
            self.model.save_model(save_path)

        self.model.eval()

        valid_loss = 0
        valid_acc = 0

        with torch.no_grad():
            for data, label in tqdm(valid_loader, desc="Valid Iter", disable=dry_run):
                data, label = data.to(self.args.device), label.to(self.args.device)
                pred = self.model(data)

                loss = self.loss_fn(pred, label)
                acc = (torch.argmax(pred, dim=-1) == label).float().mean().item()

                valid_loss += loss.item()
                valid_acc += acc

        self.model.train()

        return valid_loss / len(valid_loader), valid_acc / len(valid_loader)

