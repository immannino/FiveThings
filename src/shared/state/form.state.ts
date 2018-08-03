import { State, Action, StateContext, Selector } from '@ngxs/store';

export class SetFormData {
    static readonly type = '[Form] Set FormData';
    constructor(public authData: any) {}
}

@State({
  name: "form",
  defaults: {
      entryForm: {
        model: undefined,
        dirty: false,
        status: "",
        errors: {}
      }
  }
})
export class FormState {
  @Selector() static _toggleDrinks(state: any) {
    return state.toggleDrinks;
  }

  @Action(SetFormData)
  setFormData(ctx: StateContext<any>, action: SetFormData) {}
}