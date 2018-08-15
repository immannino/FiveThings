import { State, Action, StateContext, Selector } from '@ngxs/store';

export class SetFormData {
    static readonly type = '[Form] Set FormData';
    constructor(public formData: any) {}
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
  @Action(SetFormData)
  setFormData(ctx: StateContext<any>, action: SetFormData) {
    const localState = ctx.getState();

    ctx.patchState({
      ...localState,
      formData: action.formData
    });
  }
}