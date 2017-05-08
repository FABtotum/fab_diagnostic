<?php
/**
 * 
 * @author Daniel Kesler
 * @version 0.10.0
 * @license https://opensource.org/licenses/GPL-3.0
 * 
 */
?>

<div class="tab-content padding-10">
<?php echo $tabs_content;?>
</div>

<!-- SETTINGS MODAL -->
<div class="modal fade" tabindex="-1" role="dialog" id="logsModal">
	<div class="modal-dialog modal-lg" role="document">
		<div class="modal-content">

			<div class="modal-header">
				<button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
				<h4 class="modal-title">Logs</h4>
			</div><!-- /.modal-header -->

			<div class="modal-body">
				
			</div><!-- /.modal-body -->

			<div class="modal-footer">
			<button type="button" class="btn btn-default task-action" data-action="download-log" title="Downlaod log files"><i class="fa fa-download"></i> <?php echo _("Download");?></button>
			<button type="button" class="btn btn-primary" data-action="close" data-dismiss="modal"><i class="fa fa-save"></i> <?php echo _("Close");?></button>
			</div><!-- /.modal-footer -->

		</div><!-- /.modal-content -->
	</div><!-- /.modal-dialog -->
</div><!-- /.modal -->
