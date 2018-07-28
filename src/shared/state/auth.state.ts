import { State, Action, StateContext, Selector } from '@ngxs/store';

export class SetAuth {
    static readonly type = '[Auth] Set Auth';
    constructor(public authData: any) {}
}

@State({
  name: "survey",
  defaults: {
      authData: {

      }
  }
})
export class AuthState {
  @Selector() static _toggleDrinks(state: any) {
    return state.toggleDrinks;
  }

  @Action(SetAuth)
  setAuth(ctx: StateContext<any>, action: SetAuth) {
    const localState = ctx.getState();

    ctx.patchState({
      ...localState,
      userAccessToken: action.authData.userAccessToken,
      token_type: action.authData.token_type,
      refreshTokenTimeout: action.authData.refreshTokenTimeout,
      state: action.authData.state
    });
  }
}