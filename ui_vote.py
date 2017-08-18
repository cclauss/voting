import ui
from pyui_utils import PYUILoader
from fake_backend import fake_vote_record

_user_vote_ui_file = 'user_vote'

class UserVote(PYUILoader):
    '''
    '''
    def __init__(self, ui_filename, vote_data, *args, **kwargs):
        self.vote_data = vote_data
        super().__init__(ui_filename, *args, **kwargs)
    
    def did_load(self):
        '''
        OK, the UIFile has loaded, now we can populate the form.
        This event is fired by the ui module.
        '''
        vd = self.vote_data  # quick reference to our data
        
        # add all instance vars for the form elements to the class.
        # its ok, but the late binding means the editor can not help
        # still better than string indexs I think.
        # This is not recursive. I could be though.
        [self.__dict__.update({sv.name:sv}) for sv in self.subviews]
        
        self.category.text = vd.category
        self.question.text = vd.question
        self.answers.data_source = self.create_list_data()
        self.answers.size_to_fit()
        self.total_votes.text = str(vd.total_votes)
        
    def create_list_data(self):
        items = [{**ans} for ans in self.vote_data.answers]
        lds = ui.ListDataSource(items)
        return lds
if __name__ == '__main__':
    vote_data = fake_vote_record()
    v = UserVote(_user_vote_ui_file, vote_data, name='Vote')
    v.present('sheet', animated=False)
    
