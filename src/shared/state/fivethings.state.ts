import { State, Action, StateContext, Selector } from '@ngxs/store';

export class SetFivethings {
    static readonly type = '[Auth] Set Fivethings';
    constructor(public entries: string[]) {}
}

@State({
  name: "fivethings",
  defaults: {
      entries: []
  }
})
export class FivethingsState {
  @Selector() static _toggleDrinks(state: any) {
    return state.toggleDrinks;
  }

  @Action(SetFivethings)
  setFivethings(ctx: StateContext<any>, action: SetFivethings) {
    const localState = ctx.getState();

    ctx.patchState({
      ...localState,
      entries: action.entries
    });
  }
}