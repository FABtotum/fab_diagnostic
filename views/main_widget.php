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

<!-- LOGS MODAL -->
<div class="modal fade" tabindex="-1" role="dialog" id="logsModal">
	<div class="modal-dialog modal-lg" role="document">
		<div class="modal-content">

			<div class="modal-header">
				<button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
				<h4 class="modal-title"><?php echo dgettext('fab_diagnostics', 'Logs');?></h4>
			</div><!-- /.modal-header -->

			<div class="modal-body" id="log-content">
				
			</div><!-- /.modal-body -->

			<div class="modal-footer">
			<button type="button" class="btn btn-default task-action" data-action="download-log" title="Downlaod log files"><i class="fa fa-download"></i> <?php echo dgettext("fab_diagnostic", "Download");?></button>
			<button type="button" class="btn btn-primary" data-action="close" data-dismiss="modal"><i class="fa fa-save"></i> <?php echo dgettext("fab_diagnostic", "Close");?></button>
			</div><!-- /.modal-footer -->

		</div><!-- /.modal-content -->
	</div><!-- /.modal-dialog -->
</div><!-- /.modal -->

<!-- INTERACTIVE MODAL -->
<div class="modal fade" tabindex="-1" role="dialog" id="testcaseModal">
	<div class="modal-dialog modal-lg" role="document">
		<div class="modal-content">

			<div class="modal-header">
				<h4 class="modal-title">TestCase</h4>
			</div><!-- /.modal-header -->

			<div class="modal-body">
				<div class="row" id="modal-graph" style="display:none">
					<div id="temperatures-chart" style="margin-top:0px;width: 100%;" class="chart"> </div>
				</div>
				<div class="row" id="modal-trace" style="display:none">
					<div class="textarea-div">
						<div class="typearea">
							<div class="custom-scroll trace-console" ><?php echo dgettext("fab_diagnostic", "Loading...");?></div>
						</div>
					</div>
				</div>
			</div><!-- /.modal-body -->

			<div class="modal-footer">
			</div><!-- /.modal-footer -->

		</div><!-- /.modal-content -->
	</div><!-- /.modal-dialog -->
</div><!-- /.modal -->
